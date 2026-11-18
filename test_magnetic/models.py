from django.db import models

# Create your models here.

class System(models.Model):
    sys_name = models.CharField(max_length=200,null=True)
    chem_formula = models.CharField(max_length=20,null=True)
    space_grp = models.CharField(max_length=10,null=True)
    space_grp_no = models.IntegerField(null=True)
    publication = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.chem_formula + ' - ' + self.space_grp


class Structure(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    chem_form_full = models.CharField(max_length=20,null=True)
    nelements = models.IntegerField(null=True)
    telements = models.JSONField()
    lat_param = models.FloatField(null=True)
    length_unit = models.CharField(max_length=20,null=True)
    lat_basis_vec = models.JSONField(null=True)
    dimension = models.CharField(max_length=20,null=True)
    periodicity = models.JSONField(null=True)
    site_pos = models.JSONField(null=True)
    code = models.CharField(max_length=20,null=True)

#    def __str__(self):
#        return self.system

class MagGenInfo(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    mag_gs = models.CharField(max_length=25,null=True)
    mag_atoms = models.JSONField(null=True)
    nmag_atoms = models.IntegerField(null=True)
    mag_mom_cell = models.FloatField(null=True)
    mag_mom_site = models.JSONField(null=True)
    moment_unit = models.CharField(max_length=5,null=True)

class MagBondData(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    bond_type = models.IntegerField(null=True)
    bond_shell = models.IntegerField(null=True)
    bond_pair = models.CharField(max_length=10,null=True)
    bond_dist = models.FloatField(null=True)
    bond_vec  = models.JSONField(null=True)
    length_unit = models.CharField(max_length=10,null=True)


class MagExchangeData(models.Model):
    magbonddata = models.ForeignKey(MagBondData, on_delete=models.CASCADE)
    exchange_unit = models.CharField(max_length=10,null=True)
    exchange_tensor = models.JSONField(null=True)
    Jiso = models.JSONField(null=True)
    Janiso = models.JSONField(null=True)
    DMI = models.JSONField(null=True)
    SIA = models.JSONField(null=True)
