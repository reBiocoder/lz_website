import asyncio
import os

from Bio import SeqIO


class Homologous:
    """
    调用服务器内部shell
    """

    def __init__(self, locus_tag):
        self.locus_tag = locus_tag

    def command(self):
        return "echo '200408@abc!' | sudo -S bash prepare.sh " + str(self.locus_tag)
        # return "sudo bash prepare.sh " + str(self.locus_tag)

    async def shell(self):
        proc = await asyncio.create_subprocess_shell(
            self.command(),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        return proc.returncode, stdout.decode(), stderr.decode()

    async def file_to_json(self, status_code, stdout=None, stderr=None):
        """
        status_code: shell返回状态码
        stdout: 脚本的输出内容
        ['/home/xiaoming/HomologsBP_OUT/AOY38_RS11550.1594435896374.out6', '1594435896374', '']
        stderr: 错误输出
        """
        stdout_list = str(stdout).split('\n')
        timestamp = stdout_list[1]  # 文件夹对应时间戳
        result = {}
        if status_code == 0 and stdout:  # 正常返回
            file_path = stdout_list[0]
            table_key = []  # 表格的头
            table_res = []  # 保存所有数据
            with open(str(file_path), 'r') as f:
                for i, line in enumerate(f.readlines()):
                    strip_list = line.strip().split(sep='\t')
                    if i == 0:
                        table_key = strip_list
                    else:
                        tmp = {}
                        for j in range(len(table_key)):
                            try:
                                tmp[table_key[j]] = strip_list[j]
                            except:
                                tmp[table_key[j]] = ""
                        table_res.append(tmp)
            result["header"] = table_key
            result['data'] = table_res
            result["code"] = 1  # 正确的输出
            dir_path = os.path.dirname(file_path)
            tmp_file = str(self.locus_tag) + '.' + str(timestamp) + '.*'
            current_path = os.path.join(dir_path, tmp_file)
            command = 'sudo rm -rf ' + str(current_path)
            await asyncio.create_subprocess_shell(command)  # 删除相关文件
            return result
        else:
            result["code"] = 0  # 错误输出a
            result["error"] = stderr
            return result


class Sequence:
    def __init__(self, refseq_no, chr, start, end, Lstart, Lend, strand):
        self.refseq_no = refseq_no
        self.chr = chr
        self.start = int(start)
        self.end = int(end)
        self.Lstart = int(Lstart)
        self.Lend = int(Lend)
        self.strand = strand

    def rev(self, seq):
        base_trans = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C', 'a': 't', 'c': 'g', 't': 'a', 'g': 'c'}
        rev_seq = list(reversed(seq))
        rev_seq_list = [base_trans[k] for k in rev_seq]
        rev_seq = ''.join(rev_seq_list)
        return rev_seq

    def file_path(self):
        base_path = '/home/xiaoming/Homologs/data'
        # base_path = '/Users/sophia/PycharmProjects/lz/server'
        current_path = os.path.join(base_path, self.refseq_no)
        file_name = ''
        for root, dirs, files in os.walk(current_path):  # 该目录下只存在一个文件
            file_name = files[0]
        file_path = os.path.join(current_path, file_name)
        return file_path

    def get_json_data(self):
        """
        得到核酸序列
        :return:
        """
        title = '>' + str(self.refseq_no) + ' [' + str(self.chr) + ':' + str(self.start) + '..' + \
                str(self.end) + '; ' + str(self.strand) + ' ; ' + str(int(self.end) - int(self.start) + 1) \
                + 'bp]'
        fna_dict = SeqIO.to_dict(SeqIO.parse(self.file_path(), 'fasta'))
        sub_seq = fna_dict[self.chr].seq[self.start - 1: self.end]
        if self.strand == '+':
            # 判断相交区间
            if self.end >= self.Lstart and self.Lend >= self.start:  # 存在相交区间
                if self.start >= self.Lstart:
                    color_start = 0  # self.start 所求为下标
                else:
                    color_start = self.Lstart - self.start
                if self.end >= self.Lend:
                    color_end = self.Lend - self.start + 1  # self.Lend 考虑循环时，最后的下标要加1
                else:
                    color_end = self.end - self.start + 1
            else:
                color_start, color_end = -1, -1
        else:  # 反链，反向互补
            sub_seq = self.rev(sub_seq)
            # 判断相交区间
            if self.end >= self.Lstart and self.Lend >= self.start:  # 存在相交区间
                if self.start >= self.Lstart:  # 反向互补，
                    color_end = self.end - self.start + 1
                else:
                    color_end = (self.end - self.start) - (self.Lstart - self.start) + 1
                if self.end >= self.Lend:
                    color_start = self.end - self.Lend
                else:
                    color_start = 0
            else:
                color_start, color_end = -1, -1
        color_len = color_end - color_start
        res = {"color_len": color_len, "title": title, "seq": str(sub_seq), 'color_start': color_start, 'color_end': color_end}
        return res

    async def get_faa_data(self, locus_tag):
        """
        得到该locus_tag对应的核酸序列
        :param locus_tag:
        :return:
        """
        base_path = '/home/xiaoming/Homologs'
        # base_path = '/Users/sophia/PycharmProjects/lz/server'
        file_path = os.path.join(base_path, 'cyano_db_20200611.faa')
        cmd = "grep " + str(locus_tag) + " -A 1 " + file_path
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )  # 异步运行grep命令查找相应数据， 防止系统阻塞
        stdout, stderr = await proc.communicate()
        temp_list = stdout.decode('utf-8').split('\n')
        faa_title = temp_list[0]
        faa_content = temp_list[1]
        return faa_title, faa_content
        # # ##### 开发测试代码##########
        # faa_title = '>GKIL_RS00780|GCF_000484535.1'
        # faa_content = """MTTLVATTPVTYPSGDGRPLAETFLHVYAILTTLEVLRQYLEGSQATVLANQFLYYAPGVRTSRVAPDVMVIFGVAPGPRDSYKTWEEGQVPAIIFEITSESTRSKDQDDKLRLYEFLGVQEYWLFDPKGEWIQDKLRGYRLQVIEQGDGPVNHYQLIEENISERLQLRLQVEGELIGFYRLDNSQKLLIPSELAAELRATAAQLEQSEQRAQAAEQRAQAAEAVVQQEQQARQQAEQRAAELAERLRELGIDPDTP"""
        # return faa_title, faa_content


class Interproscan(Homologous):
    def __init__(self, ref_no, locus_tag):
        super(Interproscan, self).__init__(locus_tag)
        self.ref_no = ref_no

    def command(self):
        return "echo '200408@abc!' | sudo -S bash interpro_prepare.sh " + \
               str(self.ref_no) + " " +str(self.locus_tag)
        #  开发代码
        # return "echo '19990120' | sudo -S bash interpro_prepare.sh " + \
        #        str(self.ref_no) + " " +str(self.locus_tag)

    async def package_result(self):
        result = {}
        code, stdout, stderr = await self.shell()  # 异步调用shell
        if code == 0:
            result['code'] = 1
            result['msg'] = 'successful!'
            result['name'] = str(self.locus_tag) + '.html'
        else:
            result['code'] = 0
            result['msg'] = 'opps, no hits found...'
            result['name'] = ''
        return result


if __name__ == '__main__':
    # a = Sequence('GCF_000464785.1', 'NZ_KE734717.1', '14449', '17067',
    #              '14449', '17067', '+')
    # print(a.get_json_data())
    loop = asyncio.get_event_loop()
    a = Interproscan('GCF_000484535.1', 'GKIL_RS00780')
    loop.run_until_complete(a.package_result())
