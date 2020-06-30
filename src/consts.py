class Consts:
    __slots__ = (
        "latent_length",
        "pre_length",
        "Pd",
        "R0",
        "Pi", # chance to be sick
        "Rl" # time until results
    )

    def __init__(self,
                 latent_length: int = 3,
                 pre_length: int = 3,
                 Pd: float = 0.7,
                 R0: float = 2.0,
                 P_per_milion_per_week = 1500,
                 Rl: int = 1
                 ):
                    self.latent_length = latent_length
                    self.pre_length = pre_length
                    self.Pd = Pd
                    self.R0 = R0
                    self.Pi = P_per_milion_per_week / 7 * (latent_length + pre_length) / 1e6
                    self.Rl = Rl

    def __str__(self):
        return f"latent length: {self.latent_length}, presymptomatic length: {self.pre_length}," \
               "Pd: {self.Pd} " \
               f"R0: {self.R0}, Pi: {self.Pi}, Rl: {self.Rl}"

    @property
    def total_length(self):
        return self.latent_length + self.pre_length

    @property
    def daily_R0(self):
        return self.R0 / self.pre_length


if __name__ == "__main__":
    defaults = Consts()
    print(defaults)
    non_defaults = Consts(R0=3, Rl=0, Pd=0.8, P_per_milion_per_week=2000)
    print(non_defaults)
