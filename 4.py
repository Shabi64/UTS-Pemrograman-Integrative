class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):

        height_meters = self.height * 0.3048

        weight_kg = self.weight * 0.453592

        bmi = weight_kg / (height_meters ** 2)
        return bmi

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Main class
if __name__ == "__main__":

    person1 = BMI(150, 5.5)  
    person2 = BMI(160, 5.7) 

    bmi_person1 = person1.BMI_Value()
    bmi_person2 = person2.BMI_Value()

    print("BMI for person 1:", bmi_person1)
    print("BMI for person 2:", bmi_person2)

    if person1 == person2:
        print("Person 1 and Person 2 have the same weight and height.")
    else:
        print("Person 1 and Person 2 have different weight and/or height.")
