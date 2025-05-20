from scapy.all import sniff, IP, TCP, UDP, Raw, get_if_list

def process_packet(packet):
    print("="*60)
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[IP] {ip_layer.src} -> {ip_layer.dst} (Proto: {ip_layer.proto})")
        
        if TCP in packet:
            print(f"[TCP] {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"[UDP] {packet[UDP].sport} -> {packet[UDP].dport}")

        if Raw in packet:
            try:
                print("[Payload]:", packet[Raw].load.decode('utf-8', errors='ignore'))
            except:
                print("[Payload]: (binary data)")

def main():
    print("Available interfaces:", get_if_list())  # Helpful for testing
    print("Sniffer started... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()

