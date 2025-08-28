try:
    exec("if (20 < 30) print('20 is less than 30')")
except SyntaxError as e:
    print("Caught a syntax error:", e)
except Exception as e:
    print("Caught a different error:", e)