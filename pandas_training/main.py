from getting_started.importing import import_pandas
from getting_started.series import main as series_demo
from getting_started.dataframe import main as dataframe_demo
from getting_started.csv_operations import demo_csv_operations

from data_inspection.viewing_data import main as viewing_demo
from data_inspection.dataframe_info import main as info_demo
from data_inspection.statistics import main as statistics_demo
from data_inspection.unique_and_counts import main as counts_demo
from selection_filtering.column_selection import main as column_demo
from selection_filtering.row_selection import main as row_demo
from selection_filtering.filtering import main as filtering_demo
from selection_filtering.multiple_conditions import main as conditions_demo

from data_cleaning.missing_values import main as missing_demo
from data_cleaning.fill_drop_nulls import main as fill_demo
from data_cleaning.datatype_conversion import main as datatype_demo
from data_cleaning.add_modify_columns import main as modify_demo
from data_cleaning.rename_drop import main as rename_demo
from data_cleaning.duplicates import main as duplicate_demo

from grouping_sorting.sorting import main as sorting_demo
from grouping_sorting.groupby import main as groupby_demo
from grouping_sorting.merge import main as merge_demo
from grouping_sorting.concat import main as concat_demo

from selection_filtering.column_selection import main as column_demo
from selection_filtering.row_selection import main as row_demo
from selection_filtering.filtering import main as filtering_demo
from selection_filtering.multiple_conditions import main as conditions_demo

def main():
    print("=" * 70)
    print("GETTING STARTED")
    print("=" * 70)

    import_pandas()
    series_demo()
    dataframe_demo()
    demo_csv_operations()

    print("\n" + "=" * 70)
    print("DATA INSPECTION")
    print("=" * 70)

    viewing_demo()
    info_demo()
    statistics_demo()
    counts_demo()

    print("\n" + "=" * 70)
    print("SELECTION AND FILTERING")
    print("=" * 70)

    column_demo()
    row_demo()
    filtering_demo()
    conditions_demo()
    print("\n" + "=" * 70)

    print("DATA CLEANING")
    print("=" * 70)
    missing_demo()
    fill_demo()
    datatype_demo()
    modify_demo()
    rename_demo()
    duplicate_demo()
    print("\n" + "=" * 70)
    print("GROUPING & SORTING")
    print("=" * 70)

    sorting_demo()
    groupby_demo()
    merge_demo()
    concat_demo()
if __name__ == "__main__":
    main()