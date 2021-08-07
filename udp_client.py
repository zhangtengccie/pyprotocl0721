import socket
import pickle
import struct
import hashlib
def udp_send_data(ip,port,data_list):
    address = (ip,port)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1

    for x in data_list:
        send_data = pickle.dumps(x)
        m = hashlib.md5()
        m.update(send_data)
        md5_value = m.hexdigest()
        pkg_head = struct.pack('>hhii',version,pkt_type,seq_id,len(send_data))
        pkg= pkg_head + send_data+md5_value.encode()
        s.sendto(pkg,address)

        seq_id +=1

    s.close()


if __name__ == '__main__':
    user_data = ['乾颐堂',[1,'qytang',3],{'qytang':1,'test':3}]
    udp_send_data('192.168.77.4',6666,user_data)


