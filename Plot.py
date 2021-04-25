import matplotlib.pyplot as plt

fig=plt.figure()

axes=fig.add_axes([0,0,1,1])

langs=['C','C++','Java','PHP','Python']

students=[23,17,35,29,12]

axes.bar(langs,students)

plt.show()