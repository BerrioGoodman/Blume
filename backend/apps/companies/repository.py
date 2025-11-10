from .models import companyModel

class CompanyRepository:
    def save(self, company):
        obj = companyModel.objects.create(
            id=company.id,
            nombre_empresa=company.nombre_empresa,
            sector_industria=company.sector_industria,
            direccion=company.direccion,
            telefono=company.telefono
        )
        return obj 