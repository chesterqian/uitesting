from sgw_db_operator import SgwDataBaseOperator
from cif_db_operator import CifDbOperator
# uat:supergw_uat/cif_uat
# perf:spw/cif
sgw_database_operator = SgwDataBaseOperator('supergw_uat')
cif_database_operator = CifDbOperator('cif_uat')