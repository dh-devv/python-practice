
def sate_divide(a, b):

    try:
        return a/ b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "숫자만 입력 가능합니다."
    except Exception as e:
        return f"알 수 없는 에러가 발생했습니다. {e}"

    finally:
        print("연산이 종료되었습니다.")

def calculate(a, b, op):
    op_list = ["+", "-", "*", "/"]

    if op not in op_list:
        return "연산자 입력 오류"

    if op == '+':
        return a + b
    
    elif op == '-':
        return sate_divide(a, b)

    elif op == '*':
        return a * b

    elif op == '/':
        try:
            return a / b

        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다."

        except TypeError:
            return "숫자만 입력 가능합니다."
            
        except Exception as e:
            return f"알 수 없는 에러가 발생했습니다. {e}"