import csv
print('Hi there,What do you wanna do?')
print('1.Add new meeting Information')
print('2.Search for meeting information')
print('Enter 1 or 2 to take action')
ask = input()
if ask == '1':

    print("Hey,you've your meeting today? That's great!Let me help you keeping your meeting data save.")
    date = input('Enter the meeting date: ')
    start_time = input('When the meeting has started?: ')
    meetingstartedby = input('Who has started the meeting?: ')
    tmd = input('Who is the Toastmaster of the day?: ')
    theme = input('What is the meeting theme today?? ')
    bps = input('Who is the best prepared speaker today?: ')
    bts = input('Who is the best table topic speaker today?: ')
    bev = input('Who is the best evaluator today?: ')
    brp = input('Who is the best role player today?: ')
    importantevent = input(
        'Is there any important event happend today?;')
    meeting_endtime = input('When the meeting has ended?: ')
    reminder = input('Do you wanna add a reminder for the next meeting?: ')
    with open('database.csv', 'a') as f:
        newdata = csv.writer(f)
        newdata.writerow([date,
                          start_time,
                          meetingstartedby,
                          tmd,
                          theme,
                          bps,
                          bts,
                          bev,
                          brp,
                          importantevent,
                          meeting_endtime,
                          reminder])
elif ask == '2':
    dateforsearch = input(
        'Enter the date of meeting or type "last Meeting" to get the information of last meeting: ')
    with open('database.csv', 'r') as f:
        special1 = csv.reader(f)
        if 'last' in dateforsearch.lower():
            options = list(special1)[0]
            with open('database.csv', 'r') as f2:
                special12 = csv.reader(f2)
                maindata = list(special12)[-1]
                for j, k in zip(options, maindata):
                    print(f'{j}: {k}')
                    print('')

        readdata = csv.DictReader(f)
        for x in readdata:
            if x['Meeting Date'] == dateforsearch:
                for j, k in x.items():
                    print(f'{j}: {k}')
                    print('')

            else:
                print('Sorry,there is no meeting information on that day.')


else:
    print("Hey,you didn't enter a valid number.Please try again.Thank you")
