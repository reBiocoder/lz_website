import asyncio
import os
import shutil


class Homologous:
    def __init__(self, locus_tag):
        self.locus_tag = locus_tag

    def command(self):
        # return "echo '******' | sudo -S bash prepare.sh " + str(self.locus_tag)
        return "sudo bash prepare.sh " + str(self.locus_tag)

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


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    a = Homologous('TX50_RS00020')
    stdcode, stdout, stderr = loop.run_until_complete(a.shell())
    print(a.file_to_json(stdcode, stdout, stderr))

