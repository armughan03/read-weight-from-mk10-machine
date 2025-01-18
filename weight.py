from server.utils.read_weight import read_weight

if __name__ == "__main__":
    weight = read_weight()
    if weight:
        weight = float(weight)
        print(f"Final stable weight reading: {weight} KG")
    else:
        print("Failed to get a stable reading.")
