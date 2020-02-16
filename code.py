if chosen_arrangement_first_three_themes= economy, environment, energy
then selected_party=partyA

if chosen_arrangement_first_three_themes= environment, energy, transport
then selected_party=partyB

if chosen_arrangement_first_three_themes= economy, environment, agriculture
then selected_party=partyC

if chosen_arrangement_first_three_themes= immigration, safety, health care
then selected_party=partyD

if chosen_arrangement_first_three_themes= education, science, culture
then selected_party=partyE

if chosen_arrangement_first_three_themes= immigration, economy, infrastructure
then selected_party=partyF

if chosen_arrangement_first_three_themes= economy, infrastructure, transport
then selected_party=partyG

# Give parties a label with a local party name for displaying purposes
partyA= set_local_party_name_here
partyB= set_local_party_name_here
partyC= set_local_party_name_here
partyD= set_local_party_name_here
partyE= set_local_party_name_here
partyF= set_local_party_name_here
partyG= set_local_party_name_here

# Display chosen party
if selected_party=partyA
Then display "You have chosen for [display label:partyA]"
if selected_party=partyB
Then display "You have chosen for [display label:partyB]"
if selected_party=partyC
Then display "You have chosen for [display label:partyC]"
if selected_party=partyD
Then display "You have chosen for [display label:partyD]"
if selected_party=partyE
Then display "You have chosen for [display label:partyE]"
if selected_party=partyF
Then display "You have chosen for [display label:partyF]"
if selected_party=partyG
Then display "You have chosen for [display label:partyG]"

# Now start the questions on the chosen themes for increased opinion precision
If chosen_arrangement_first_three_themes includes economy
then launch q10r_economyquestions

If chosen_arrangement_first_three_themes includes environment
then launch q10r_environmentquestions

If chosen_arrangement_first_three_themes includes energy
then launch q10r_energyquestions

If chosen_arrangement_first_three_themes includes transport
then launch q10r_transportquestions

If chosen_arrangement_first_three_themes includes immigration
then launch q10r_immigrationquestions

If chosen_arrangement_first_three_themes includes safety
then launch q10r_safetyquestions

If chosen_arrangement_first_three_themes includes health care
then launch q10r_healthcarequestions

If chosen_arrangement_first_three_themes includes education
then launch q10r_educationquestions

If chosen_arrangement_first_three_themes includes science
then launch q10r_sciencequestions

If chosen_arrangement_first_three_themes includes culture
then launch q10r_culturequestions

If chosen_arrangement_first_three_themes includes infrastructure
then launch q10r_culturequestions

If chosen_arrangement_first_three_themes includes agriculture
then launch q10r_culturequestions
