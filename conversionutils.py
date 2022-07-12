class ConversionUtils(object):
    IMPERIAL = 1
    METRICS = 2
    MPG = 0
    MPG_SUFFIX = "MPG"
    L_PER_100KM = 1
    L_PER_100KM_SUFFIX = "l/100km"
    L_PER_KM = 2
    L_PER_KM_SUFFIX = "l/km"

    # Canadian unit
    GALLON_VOLUME = 4.546
    MAGIC_NUMBER = 282.481

    @staticmethod
    def convert_mpg_to_l100km(mpg: float) -> float:
        """
        Convert MPG to l/100km
        :param mpg: MPG value
        :return: l/100km value
        """
        return round(ConversionUtils.MAGIC_NUMBER / mpg, 2)

    @staticmethod
    def convert_l100km_to_mpg(l100km: float) -> float:
        """
        Convert l/100km to MPG
        :param l100km: l/100km value
        :return: MPG value
        """
        return round(ConversionUtils.MAGIC_NUMBER / l100km, 2)

    @staticmethod
    def convert_mpg_to_lkm(mpg: float) -> float:
        """
        Convert MPG to l/km
        :param mpg: MPG value
        :return: l/km value
        """
        return round(ConversionUtils.MAGIC_NUMBER / (mpg * 10), 5)

    @staticmethod
    def convert_lkm_to_mpg(lkm: float) -> float:
        """
        Convert l/km to MPG
        :param lkm: l/km value
        :return: MPG value
        """
        return round(ConversionUtils.MAGIC_NUMBER / (lkm * 10), 2)

    @staticmethod
    def convert_m_to_km(meters: float) -> float:
        """
        Convert meters to kms
        :param meters: Meters value
        :return: Kms value
        """
        return round(meters / 1000, 2)

    @staticmethod
    def convert_m_to_miles(meters: float) -> float:
        """
        Convert meters to miles
        :param meters: Meters value
        :return: Miles value
        """
        return round(meters / 1609, 2)

    @staticmethod
    def get_suffix(metric_choice: int) -> str:
        """
        Get suffix per metric choice
        :param metric_choice: Metric choice
        :return: Suffix
        """
        if metric_choice == ConversionUtils.MPG:
            return ConversionUtils.MPG_SUFFIX
        elif metric_choice == ConversionUtils.L_PER_100KM:
            return ConversionUtils.L_PER_100KM_SUFFIX
        elif metric_choice == ConversionUtils.L_PER_KM:
            return ConversionUtils.L_PER_KM_SUFFIX
        else:
            return ""

