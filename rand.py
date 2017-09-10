import string
import random

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    print ''.join(random.choice(chars) for _ in range(size))
	
#if __name__ == "__main__":
#    main()
id_generator()