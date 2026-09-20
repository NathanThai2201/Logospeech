
import Logospeech as L

ascii_low = 32
ascii_high = 126

def step(master, seed):

    curr = L.v(master, seed)
    curr.reverse()
    curr = L.d(curr,0)
    curr = curr+curr
    curr = L.v(curr, seed)
    curr.reverse()
    curr = L.d(curr,0)
    return "".join(curr)

def main():

    print("hello world")

    name = "Atmospherus"

    seeds = [
        "1244533",
        "2435533",
        "0195739"
    ]


    evolutions = []

    for i in range(len(seeds)):

        curr = step(name, seeds[i])

        ALLOWED = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
            "!@#$%^&*=?-+<>"
        )

        curr = "".join(c for c in curr if c in ALLOWED)

        evolutions.append(
            seeds[i] + ": " + curr
        )

    print(evolutions)

    with open("in.txt", "w") as file:
        for e in evolutions:
            file.write(e + "\n")

    return 0


if __name__ == "__main__":
    main()

