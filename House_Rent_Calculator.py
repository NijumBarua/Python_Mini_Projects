Fixed_House_Rent = 7000
Charge_per_unit = 10

Bazar_cost_this_month = int(input("Put this months total bazar cost (In Numbers): "))
Electricity_Unit = int(input("Enter the unit of this month (In Numbers): "))
Room_member_count = int(input("Enter the number of room members (In Numbers): "))


Electrivity_Bill = Electricity_Unit * Charge_per_unit

Total_Bill_for_each_persons = (Fixed_House_Rent + Electrivity_Bill + Bazar_cost_this_month) / Room_member_count

print(f"A single room member has to pay  {Total_Bill_for_each_persons}")

