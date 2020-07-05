import motor.motor_asyncio
import asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(host='124.70.143.103', port=27010, username="root", password="200408@abc!", authSource="admin")
handle = client["lz_database"]["cyano_all_gff"]
print(handle)

async def test1():
    a = await handle.delete_many({})
    print(a)
# async def test():
#     table_key = []
#     with open("CyanoAllGFF.tab", 'rb') as f:
#         print("开始读取文件")
#         for i,line in enumerate(f):
#             table_res = []
#             if i == 0:
#                 table_key = line.decode("utf-8").strip().split(sep='\t')
#                 print(table_key)
#             else:
#                 tmp = {}
#                 for j in range(len(table_key)):
#                     tmp[table_key[j]] = line.decode("utf-8").strip().split(sep='\t')[j]
#                 print("当前正在处理{}条数据:{}\n".format(i, line.decode("utf-8").strip().split(sep='\t')))
#                 table_res.append(tmp)
#                 print("开始插入第{}条数据".format(i))
#                 await handle.insert_many(table_res)
#                 print("第{}条插入成功".format(i))
#
loop = asyncio.get_event_loop()
loop.run_until_complete(test1())