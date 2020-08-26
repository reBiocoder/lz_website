import os
import Bio
from Bio import SeqIO
import asyncio

async def a():
    path = 'cyano_db_20200611.faa'
    cmd = "grep " + "GKIL_RS00340" + " -A 1 " + path
    # res = os.popen(cmd).readlines()
    # print(res)

    proc = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
    stdout, stderr = await proc.communicate()
    result = stdout.decode('utf-8')
    temp_list = result.split('\n')
    faa_title = temp_list[0]
    faa_content = temp_list[1]
    print(temp_list)

asyncio.get_event_loop().run_until_complete(a())
