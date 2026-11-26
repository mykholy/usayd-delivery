"""Reference algorithm fixture tests only; app still unimplemented."""
import unittest,sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference_impl'))
from internationalization import to_minor,choose_market,resolve_local_wall_time
class InternationalReference(unittest.TestCase):
 def test_egp_minor(self):self.assertEqual(to_minor('799.00','EGP'),79900)
 def test_kwd_three_places(self):self.assertEqual(to_minor('7.500','KWD'),7500)
 def test_bhd_three_places(self):self.assertEqual(to_minor('12.010','BHD'),12010)
 def test_subminor_rejected(self):
  with self.assertRaises(ValueError):to_minor('7.5001','KWD')
 def test_negative_rejected(self):
  with self.assertRaises(ValueError):to_minor('-1.00','EGP')
 def test_ip_never_overrides_selected(self):self.assertEqual(choose_market(explicit='SA',stored='EG',coarse_ip='GB'),'SA')
 def test_unknown_country_has_no_implicit_billing(self):self.assertIsNone(choose_market())
 def test_new_york_spring_gap(self):self.assertEqual(resolve_local_wall_time(datetime(2027,3,14,2,30),'America/New_York'),[])
 def test_new_york_fall_fold(self):self.assertEqual(len(resolve_local_wall_time(datetime(2027,11,7,1,30),'America/New_York')),2)
 def test_riyadh_unique(self):self.assertEqual(len(resolve_local_wall_time(datetime(2027,3,14,14,30),'Asia/Riyadh')),1)
 def test_cairo_timezone_not_fixed_offset(self):
  x=resolve_local_wall_time(datetime(2027,1,10,14,0),'Africa/Cairo');self.assertEqual(len(x),1)
if __name__=='__main__':unittest.main()
