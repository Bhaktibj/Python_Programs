from Week2.Utility_ds.utilitis import Cal_Methods

def calendar_queue_runner():
    """
    THIS METHOD ACT AS RUNNER FOR calender_queue(month, year) METHOD
    """

    logic_obj = Cal_Methods()                      # creating object of the method class

    try:
        month = int(input('Enter Month:'))          # enter the month number
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter year:'))            # enter the year
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calendar_queue(month, year)


if __name__ == "__main__":
    calendar_queue_runner()