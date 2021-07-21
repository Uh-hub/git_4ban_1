

def check_integer(func):
    def decorated(h,w):
        if h >= 0 and w >= 0:
            print('함수 시작')
            return func(h,w)
            print('함수 끝')
        else:
            print("Error")
        return decorated


@check_integer

def triangle(h, w):
    return h*w*(1/2)

def square(h, w):
    return h*w

triangle(3, 4)
