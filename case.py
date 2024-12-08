import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Space_Corrected.csv")
n=int(input())
# Завдання 1
# Побудуйте гістограму для розподілу місій за статусом (Status Mission).
match n:
    case 1:
        print(df["Status Mission"].value_counts())
        df["Status Mission"].value_counts().plot(kind='hist')

# Завдання 2
# Побудуйте box plot, щоб порівняти кількість місій для різних компаній (Company Name).

    case 2:
        df["Company Name"].value_counts().plot(kind="box")

# Завдання 3
# Побудуйте точкову діаграму, щоб показати залежність між статусом ракети (Status Rocket) та статусом місії (Status Mission).
    case 3:
        df.plot(kind="scatter", x="Status Rocket", y="Status Mission")
# Завдання 4
# Побудуйте кругову діаграму, яка показує розподіл місій за локаціями запуску (Location).
    case 4:
        df["Location"].value_counts().plot(kind="pie")
# Завдання 5
# Побудуйте стовпчикову діаграму, щоб показати кількість запусків кожною компанією (Company Name).
    case 5:
        df["Company Name"].value_counts().plot(kind="bar")
# Завдання 6
# Побудуйте горизонтальну стовпчикову діаграму, щоб показати кількість ракет різних типів (Rocket).
    case 6:
        df[" Rocket"].value_counts().plot(kind="barh")
# Завдання 7
# Побудуйте лінійну діаграму, яка показує кількість місій у часі (Datum).
    case 7:
        temp = df["Datum"].map(lambda x: x.split(' ')[3])
        print(temp)
        temp.value_counts().plot(kind="line")
# Завдання 8
# Побудуйте гістограму для розподілу статусу ракет (Status Rocket).
    case 8:
        temp = df["Datum"].map(lambda x: x.split(' ')[3])
        print(temp)
        temp.value_counts().plot(kind="line")
# Завдання 9
# Побудуйте box plot, щоб порівняти кількість місій (Status Mission) залежно від місця запуску (Location).
    case 9:
        df["Location"].value_counts().plot(kind="box")
# Завдання 10
# Побудуйте точкову діаграму, щоб показати залежність між компанією (Company Name) та кількістю запусків.
    case 10:
        df.plot(kind="scatter", x="Company Name", y=)
plt.show()
