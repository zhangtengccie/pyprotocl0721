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
        rdata,addr = recv_source_data
        print(recv_source_data)
        header = rdata[:12]
        unppack_header=struct.unpack('>HHLL',header)
        version = unppack_header[0]
        pkt_type = unppack_header[1]
        seq_id = unppack_header[2]
        length = unppack_header[3]
        rdata = rdata[12:]
        data = rdata[:length]
        md5_recv= rdata[length:]
        m = hashlib.md5()
        m.update(header+data)
        md5_value = m.digest()

        #
        if md5_recv == md5_value:
            print('='*80)
            print('{0:<30}:{1:<30}'.format('数据来源于',str(addr)))
            print('{0:<30}:{1:<30}'.format('数据来源于',seq_id))
            print('{0:<30}:{1:<30}'.format('数据来源于',length))
            print('{0:<30}:{1:<30}'.format('数据来源于',str(pickle.loads(data))))

    except KeyboardInterrupt:
        sys.exit()
s.close()
