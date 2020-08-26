import motor.motor_asyncio
import asyncio
#123
client = motor.motor_asyncio.AsyncIOMotorClient()
handle = client["lz_database"]["new_cyano_genomes"]

# async def test1():
#     a = await handle.delete_many({})
#     print(a)
async def test():
    table_key = []
    with open("New_CyanoGenomes.tab.bk2", 'rb') as f:
        print("开始读取文件")
        for i, line in enumerate(f):
            table_res = []
            if i == 0:
                table_key = line.decode("utf-8").strip().split(sep='\t')
                print(len(table_key))
            else:
                tmp = {}
                data = line.decode("utf-8").strip().split(sep='\t')
                if len(table_key) == len(data):
                    for j in range(len(table_key)):
                        tmp[table_key[j]] = data[j]
                else:  # 只可能是14
                    for j in range(len(table_key)):
                        if j == 14:
                            tmp[table_key[j]] = ''
                print("当前正在处理{}条数据:{}\n".format(i, len(line.decode("utf-8").strip().split(sep='\t'))))
                table_res.append(tmp)
                print("开始插入第{}条数据".format(i))
                await handle.insert_many(table_res)
                print("第{}条插入成功".format(i))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
