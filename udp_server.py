import pickle
import sys
import socket
import pickle
import hashlib
import struct
print('UDP 服务器就绪！等待客户端数据！')
address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
while True:

    try:
        recv_source_data = s.recvfrom(2048)
        data_values,addr = recv_source_data
        print(data_values)
        head_values = struct.unpack('>hhii',data_values[:12])
        seq_id = head_values[2]
        length = head_values[3]
        data = data_values[12:(12+length)]
        md5_recv= data_values[(12+length):]
        m = hashlib.md5()
        m.update(data)
        md5_value = m.hexdigest()


        if md5_recv == md5_value.encode():
            print('='*80)
            print('{0:<30}:{1:<30}'.format('数据来源于',str(addr)))
            print('{0:<30}:{1:<30}'.format('数据来源于',seq_id))
            print('{0:<30}:{1:<30}'.format('数据来源于',length))
            print('{0:<30}:{1:<30}'.format('数据来源于',str(pickle.loads(data))))

    except KeyboardInterrupt:
        sys.exit()
s.close()
