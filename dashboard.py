import streamlit as st

from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2019, 'Monza', 'Q')

fastf1.Cache.enable_cache('_cache/')

session.load()
fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()

fast_ham = session.laps.pick_driver('HAM').pick_fastest()
ham_car_data = fast_ham.get_car_data()

t = lec_car_data['Time']
vCar = lec_car_data['Speed']
print(type(t), t)
print(type(t[0]))
print(type(vCar), vCar)

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='LEC')
ax.plot(ham_car_data['Time'], ham_car_data['Speed'], label = 'HAM')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
# plt.show()

st.pyplot(fig)

st.line_chart(lec_car_data, x = 'Time', y = 'Speed')