import asyncio
import os

import Bio
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
        self.start = int(start) - 1
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
        # base_path = '/home/xiaoming/Homologs/data'
        base_path = '/Users/sophia/PycharmProjects/lz/server'
        current_path = os.path.join(base_path, self.refseq_no)
        for root, dirs, files in os.walk(current_path):# 该目录下只存在一个文件
            file_name = files[0]
        file_path = os.path.join(current_path, file_name)
        return file_path

    def get_json_data(self):
        fna_dict = SeqIO.to_dict(SeqIO.parse(self.file_path(), 'fasta'))
        sub_seq = fna_dict[self.chr].seq[self.start: self.end]
        if self.strand == '-':
            sub_seq = self.rev(sub_seq)
        up_end = self.Lstart - self.start - 1
        orf_start = up_end + 1
        orf_end = self.Lend - self.start
        down_start = orf_end + 1
        if self.Lstart >= self.start and self.end >= self.Lend:
            result = sub_seq[0: up_end].lower() + "<span style='color: blue'>"+ \
                sub_seq[up_end: orf_end] + '</span>' + sub_seq[orf_end:].lower()
        elif self.Lstart < self.start < self.Lend <= self.end:
            result = "<span style='color: blue'>" + sub_seq[0: orf_end] + \
                     '</span>' + sub_seq[orf_end:].lower()
        elif self.start <= self.Lstart < self.end < self.Lend:
            result = sub_seq[0: up_end].lower() + "<span style='color: blue'>" + \
                sub_seq[up_end:] + '</span>'
        else:
            result = sub_seq






if __name__ == '__main__':
    a = Sequence('GCF_000464785.1', 'NZ_KE734717.1', '14449', '17067',
                 '14449', '17067', '+')
    a.file_path()
    # loop = asyncio.get_event_loop()
    # a = Homologous('TX50_RS00020')
    # stdcode, stdout, stderr = loop.run_until_complete(a.shell())
    # print(a.file_to_json(stdcode, stdout, stderr))

