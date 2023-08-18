from django.contrib import admin
from .models import *

admin.site.register(WindowDiscountMarkups)
admin.site.register(ExchangeRates)
# Calc
admin.site.register(WindowsCalc)
admin.site.register(LowTidesCalc)
admin.site.register(WindowsillCalc)
admin.site.register(Constructor)
admin.site.register(FlashingCalc)
admin.site.register(CasingCalc)
admin.site.register(SlopesOfMetalCalc)
admin.site.register(VisorsCalc)
admin.site.register(InternalSlopeCalc)
admin.site.register(MountingMaterialsCalc)
# Mounting
# admin.site.register(LowTidesInstallation)
# admin.site.register(WindowsillInstallation)
# admin.site.register(FlashingInstallation)
# admin.site.register(SlopesOfMetalInstallation)
# admin.site.register(VisorsInstallation)
# admin.site.register(InternalSlopeInstallation)
# markups
admin.site.register(WindowsillMarkups)
admin.site.register(LowTidesMarkups)
admin.site.register(CasingMarkups)
admin.site.register(FlashingMarkups)
admin.site.register(VisorsMarkups)
admin.site.register(SlopesOfMetalMarkups)
admin.site.register(InternalSlopeMarkups)