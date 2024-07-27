import discord
def lua():
    prefix=">"
    x=0
    while True:
        user_input = input(">")
        head = "0x"
        if user_input == "Exit" or user_input == "exit" or user_input == "EXIT":
            print("Exited. ")
            break
        if ": " not in user_input:
            print("Error: Couldn't find <:> to split. ")
        else:
            parts = user_input.split(": ")
            if len(parts) == 2:
                address = parts[0]
                hex_chain = parts[1]
                out = head + address
                if len(address) <= 3:
                    print("Address must be 4 characters. ")
                forbidden_chars = "ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ"
                for char in hex_chain:
                    if char in forbidden_chars:
                        print(f"Error: Unvalid character '{char}' found in hex chain.")
                else:
                    hex_list = hex_chain.split()
                    hex_list = ["0x" + hex for hex in hex_list]
                    inj0 = ",".join(hex_list)
                    address.join("0x")
                    print("inj0={" + f'{inj0}' + "} for i=0, " + f'{len(hex_list)} do data' + "[" + f'{out}+i' + "]=inj0[i+1] end")

lua()
