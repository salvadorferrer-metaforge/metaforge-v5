#!/usr/bin/env python3
# ============================================================================
# AUTHOR_IDENTITY_BLOCK [ROOT_ACCESS_ONLY]
# ============================================================================
# IDENTIFIER:  Salvador Ferrer
# PROJECT:     METAFORGE_v5 (Community Tools Registry)
# BOOK_REF:    "CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN"
# STATUS:      COMMUNITY_GATEWAY_ACTIVE
# ============================================================================
"""
METAFORGE v5 - License Eligibility Checker
Script para verificar la elegibilidad de una organización según
los términos de la licencia dual de METAFORGE v5.
"""

Uso:
    python check_license_eligibility.py
    python check_license_eligibility.py --employees 150 --revenue 45000000

Autor: Salvador Ferrer Moncho
Versión: 1.0.0
Licencia: Dual (Personal/Commercial)
"""

import argparse
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class LicenseType(Enum):
    """Tipos de licencia disponibles."""
    PERSONAL = "personal"
    PYME = "pyme"
    COMMERCIAL = "commercial"


@dataclass
class Organization:
    """Representa una organización para evaluación de licencia."""
    employees: int
    annual_revenue_eur: float
    balance_sheet_eur: Optional[float] = None
    is_part_of_group: bool = False
    
    def __post_init__(self):
        if self.employees < 0:
            raise ValueError("El número de empleados no puede ser negativo")
        if self.annual_revenue_eur < 0:
            raise ValueError("La facturación no puede ser negativa")


class LicenseChecker:
    """
    Verificador de elegibilidad de licencia según definición UE de PYME.
    
    Umbrales PYME (UE):
    - Empleados: < 250
    - Facturación anual: ≤ 50M€
    - Balance total: ≤ 43M€
    """
    
    # Umbrales según definición UE de PYME
    PYME_EMPLOYEES_THRESHOLD = 250
    PYME_REVENUE_THRESHOLD = 50_000_000  # 50 millones EUR
    PYME_BALANCE_THRESHOLD = 43_000_000  # 43 millones EUR
    
    # Precios de licencia comercial (anuales)
    COMMERCIAL_PRICING = {
        "starter": {"employees": (250, 500), "revenue": (50_000_000, 100_000_000), "price": 5000},
        "growth": {"employees": (500, 1000), "revenue": (100_000_000, 250_000_000), "price": 10000},
        "enterprise": {"employees": (1000, 5000), "revenue": (250_000_000, 1_000_000_000), "price": 25000},
        "enterprise_plus": {"employees": (5000, 10000), "revenue": (1_000_000_000, 5_000_000_000), "price": 50000},
        "global": {"employees": (10000, float('inf')), "revenue": (5_000_000_000, float('inf')), "price": None},
    }
    
    TRIAL_PERIOD_DAYS = 90
    
    def __init__(self, org: Organization):
        self.org = org
        self._eligibility_checked = False
        self._license_type = None
        self._pricing_tier = None
    
    def check_eligibility(self) -> LicenseType:
        """
        Determina el tipo de licencia aplicable.
        
        Returns:
            LicenseType: Tipo de licencia requerido
        """
        # Verificar si es uso personal (0 empleados, 0 revenue)
        if self.org.employees == 0 and self.org.annual_revenue_eur == 0:
            self._license_type = LicenseType.PERSONAL
            self._eligibility_checked = True
            return self._license_type
        
        # Verificar umbrales PYME
        is_pyme = (
            self.org.employees < self.PYME_EMPLOYEES_THRESHOLD and
            self.org.annual_revenue_eur <= self.PYME_REVENUE_THRESHOLD
        )
        
        # Verificar balance si está disponible
        if self.org.balance_sheet_eur is not None:
            is_pyme = is_pyme and (self.org.balance_sheet_eur <= self.PYME_BALANCE_THRESHOLD)
        
        # Verificar si pertenece a un grupo
        if self.org.is_part_of_group:
            is_pyme = False  # Los grupos empresariales generalmente no califican
        
        self._license_type = LicenseType.PYME if is_pyme else LicenseType.COMMERCIAL
        
        if self._license_type == LicenseType.COMMERCIAL:
            self._pricing_tier = self._determine_pricing_tier()
        
        self._eligibility_checked = True
        return self._license_type
    
    def _determine_pricing_tier(self) -> Optional[str]:
        """Determina el tier de precios comercial."""
        for tier, config in self.COMMERCIAL_PRICING.items():
            emp_min, emp_max = config["employees"]
            rev_min, rev_max = config["revenue"]
            
            emp_match = emp_min <= self.org.employees < emp_max
            rev_match = rev_min <= self.org.annual_revenue_eur < rev_max
            
            if emp_match or rev_match:  # Cualquiera de los dos criterios
                return tier
        
        return "global"  # Default al tier más alto
    
    def get_license_details(self) -> dict:
        """Retorna detalles completos de la licencia aplicable."""
        if not self._eligibility_checked:
            self.check_eligibility()
        
        details = {
            "organization": {
                "employees": self.org.employees,
                "annual_revenue_eur": self.org.annual_revenue_eur,
                "balance_sheet_eur": self.org.balance_sheet_eur,
                "is_part_of_group": self.org.is_part_of_group,
            },
            "license_type": self._license_type.value,
            "can_use_free": self._license_type in [LicenseType.PERSONAL, LicenseType.PYME],
            "requires_commercial_license": self._license_type == LicenseType.COMMERCIAL,
        }
        
        if self._license_type == LicenseType.COMMERCIAL:
            tier_config = self.COMMERCIAL_PRICING.get(self._pricing_tier, {})
            details["commercial_details"] = {
                "pricing_tier": self._pricing_tier,
                "annual_price_eur": tier_config.get("price"),
                "trial_period_days": self.TRIAL_PERIOD_DAYS,
                "contact": "licensing@metaforge.ai",
            }
        
        return details
    
    def print_report(self):
        """Imprime un reporte formateado."""
        details = self.get_license_details()
        
        print("=" * 70)
        print("METAFORGE v5 - REPORTE DE ELEGIBILIDAD DE LICENCIA")
        print("=" * 70)
        print()
        
        # Información de la organización
        print("📊 DATOS DE LA ORGANIZACIÓN:")
        print(f"   Empleados: {details['organization']['employees']}")
        print(f"   Facturación anual: €{details['organization']['annual_revenue_eur']:,.2f}")
        if details['organization']['balance_sheet_eur']:
            print(f"   Balance total: €{details['organization']['balance_sheet_eur']:,.2f}")
        if details['organization']['is_part_of_group']:
            print("   ⚠️  Pertenece a un grupo empresarial")
        print()
        
        # Resultado
        print("📋 RESULTADO DE LA EVALUACIÓN:")
        print(f"   Tipo de licencia: {details['license_type'].upper()}")
        print()
        
        if details['can_use_free']:
            print("✅ PUEDE USAR LA LICENCIA GRATUITA")
            print()
            print("   Condiciones:")
            print("   • Uso personal/académico o PYME")
            print("   • Modificación para uso propio permitida")
            print("   • No revender como producto standalone")
            print()
        
        if details['requires_commercial_license']:
            print("🔵 REQUIERE LICENCIA COMERCIAL")
            print()
            comm = details['commercial_details']
            print(f"   Tier: {comm['pricing_tier'].upper()}")
            if comm['annual_price_eur']:
                print(f"   Precio anual: €{comm['annual_price_eur']:,.2f}")
            else:
                print("   Precio: Contactar para presupuesto personalizado")
            print(f"   Período de prueba: {comm['trial_period_days']} días")
            print()
            print("   Contacto para licencia:")
            print(f"   📧 {comm['contact']}")
            print()
        
        # Umbrales de referencia
        print("📏 UMBRALES DE REFERENCIA (Definición UE de PYME):")
        print(f"   Empleados: < {self.PYME_EMPLOYEES_THRESHOLD}")
        print(f"   Facturación: ≤ €{self.PYME_REVENUE_THRESHOLD:,.0f}")
        print(f"   Balance: ≤ €{self.PYME_BALANCE_THRESHOLD:,.0f}")
        print()
        
        print("=" * 70)
        print("⚠️  NOTA: Este reporte es orientativo.")
        print("   La clasificación final requiere verificación documental.")
        print("   El autor se reserva el derecho de solicitar justificación.")
        print("=" * 70)


def interactive_mode():
    """Modo interactivo para ingresar datos."""
    print("=" * 70)
    print("METAFORGE v5 - VERIFICADOR DE ELEGIBILIDAD DE LICENCIA")
    print("=" * 70)
    print()
    print("Ingrese los datos de su organización:")
    print()
    
    try:
        employees = int(input("Número de empleados (FTE): ") or "0")
        revenue = float(input("Facturación anual (EUR): ") or "0")
        
        balance_input = input("Balance total (EUR) [opcional]: ")
        balance = float(balance_input) if balance_input else None
        
        group_input = input("¿Pertenece a un grupo empresarial? (s/n): ").lower()
        is_group = group_input in ['s', 'si', 'sí', 'y', 'yes']
        
        org = Organization(
            employees=employees,
            annual_revenue_eur=revenue,
            balance_sheet_eur=balance,
            is_part_of_group=is_group
        )
        
        checker = LicenseChecker(org)
        print()
        checker.print_report()
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperación cancelada.")
        sys.exit(0)


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description="Verificador de elegibilidad de licencia METAFORGE v5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Modo interactivo
  python check_license_eligibility.py
  
  # Parámetros directos
  python check_license_eligibility.py --employees 150 --revenue 45000000
  
  # Con balance
  python check_license_eligibility.py -e 200 -r 40000000 -b 35000000
        """
    )
    
    parser.add_argument(
        "-e", "--employees",
        type=int,
        help="Número de empleados (FTE)"
    )
    parser.add_argument(
        "-r", "--revenue",
        type=float,
        help="Facturación anual en EUR"
    )
    parser.add_argument(
        "-b", "--balance",
        type=float,
        help="Balance total en EUR (opcional)"
    )
    parser.add_argument(
        "-g", "--group",
        action="store_true",
        help="Pertenece a un grupo empresarial"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output en formato JSON"
    )
    
    args = parser.parse_args()
    
    # Si no se proporcionan argumentos, modo interactivo
    if args.employees is None and args.revenue is None:
        interactive_mode()
        return
    
    # Validar argumentos mínimos
    if args.employees is None or args.revenue is None:
        parser.error("Se requieren --employees y --revenue (o usar modo interactivo)")
    
    try:
        org = Organization(
            employees=args.employees,
            annual_revenue_eur=args.revenue,
            balance_sheet_eur=args.balance,
            is_part_of_group=args.group
        )
        
        checker = LicenseChecker(org)
        
        if args.json:
            import json
            details = checker.get_license_details()
            print(json.dumps(details, indent=2, ensure_ascii=False))
        else:
            checker.print_report()
            
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
