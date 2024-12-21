import prompt

if __name__ == '__main__':
    try:
        prompt.run()
    except KeyboardInterrupt:
        print("Bye")