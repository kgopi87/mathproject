import random as ran

aZ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "123457890"


class Token:

    def _new_token(seqlen):
        while True:
            newsing = ""

            for n in range(0, seqlen):

                randchar = ran.randint(0, len(aZ) - 1)
                randnum = ran.randint(0, len(num) - 1)
                choice = ran.randint(1, 2)

                if choice == 1:
                    newsing += aZ[randchar]
                else:
                    newsing += str(num[randnum])

                n += 1

            return newsing

    def token_generator(length_of_token):
        to_encrypt = Token._new_token(length_of_token)
        return to_encrypt