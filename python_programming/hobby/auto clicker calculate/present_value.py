class hand:
    power = 1
    likelyhood = 0.5675

class uppgrade(hand):
    level = 0
    price = None
    effekt = None
    present_value = None

    def __init__(self, level, price, effekt) -> None:
        self.level = level
        self.price = price
        self.effekt = effekt
        hand.power = self.power + effekt*level

    def find_present_value(self, time = 1):
        production_ps = self.power*self.likelyhood/2
        time_until_uppgrade = self.price/production_ps
        self.present_value = production_ps*time + time/time_until_uppgrade*self.effekt - time/time_until_uppgrade*self.price

stronger_arms = uppgrade(20, 434, 1)
greater_coin = uppgrade(12, 1.82*1000, 5)
knowledge = uppgrade(9, 16.02*1000, 40)
strong_fist = uppgrade(5, 183.11*1000, 500)
hand_injection = uppgrade(7, 4.17*(10**6), 10.8*1000)
brain_power = uppgrade(0, 85*(10**6), 235*1000)

stronger_arms.find_present_value()
greater_coin.find_present_value()
knowledge.find_present_value()
strong_fist.find_present_value()
hand_injection.find_present_value()
brain_power.find_present_value()

print(f"strong_arms:\t\t {round(stronger_arms.present_value)}")
print(f"greater_coin:\t\t {round(greater_coin.present_value)}")
print(f"knowledge:\t\t {round(knowledge.present_value)}")
print(f"strong_fist:\t\t {round(strong_fist.present_value)}")
print(f"hand_injections:\t {round(hand_injection.present_value)}")
print(f"brain_power:\t\t {round(brain_power.present_value)}")