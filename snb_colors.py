from __future__ import annotations


class Color:
    all = []

    def __init__(
        self,
        c50: str,
        c100: str,
        c200: str,
        c300: str,
        c400: str,
        c500: str,
        c600: str,
        c700: str,
        c800: str,
        c900: str,
        c950: str,
        name: str | None = None,
    ):
        self.c50 = c50
        self.c100 = c100
        self.c200 = c200
        self.c300 = c300
        self.c400 = c400
        self.c500 = c500
        self.c600 = c600
        self.c700 = c700
        self.c800 = c800
        self.c900 = c900
        self.c950 = c950
        self.name = name
        Color.all.append(self)

    def expand(self) -> list[str]:
        return [
            self.c50,
            self.c100,
            self.c200,
            self.c300,
            self.c400,
            self.c500,
            self.c600,
            self.c700,
            self.c800,
            self.c900,
            self.c950,
        ]


snb_red = Color(
    name="snb_red",
    c50="#FF5046",
    c100="#FF5046",
    c200="#FF5046",
    c300="#FF5046",
    c400="#FF5046",
    c500="#FF5046",
    c600="#FF5046",
    c700="#FF5046",
    c800="#FF5046",
    c900="#FF5046",
    c950="#FF5046",
)
snb_purple = Color(
    name="snb_red",
    c50="#593065",
    c100="#593065",
    c200="#593065",
    c300="#593065",
    c400="#593065",
    c500="#593065",
    c600="#593065",
    c700="#593065",
    c800="#593065",
    c900="#593065",
    c950="#593065",
)
