def ViewMore(msg, t="y", f="n"):
    while True:
        more = input(msg)
        if more in [t, f]:
            return more
        print(f"Digitação incorreta. Digite apenas {t} ou {f}")
