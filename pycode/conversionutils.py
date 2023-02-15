# Utility class
class ConversionUtils(object):
    IMPERIAL = 1
    METRICS = 2
    MPG = 0
    MPG_SUFFIX = "MPG"
    L_PER_100KM = 1
    L_PER_100KM_SUFFIX = "l/100km"
    L_PER_KM = 2
    L_PER_KM_SUFFIX = "l/km"

    GALLON_VOLUME = 4.546
    MAGIC_NUMBER = 282.481

    @staticmethod
    def convert_mpg_to_l100km(mpg: float) -> float:
        """
        Convert MPG to L/100 km
        :param mpg: MPG value
        :return: L/100 km value
        """
        return round(ConversionUtils.MAGIC_NUMBER / mpg, 2)

    @staticmethod
    def convert_l100km_to_mpg(l100km: float) -> float:
        """
        Convert L/100 km to MPG
        :param mpg: L/100km value
        :return:  MPG value
        """
        return round(ConversionUtils.MAGIC_NUMBER / l100km, 2)

    @staticmethod
    def convert_mpg_to_lkm(mpg: float) -> float:
        """
        Convert MPG to L/1 km
        :param mpg: MPG value
        :return: L/1 km value
        """
        return round(ConversionUtils.MAGIC_NUMBER / (mpg * 100), 5)

    @staticmethod
    def convert_lkm_to_mpg(lkm: float) -> float:
        """
        Convert L/1 km to MPG
        :param mpg: L/1 km value
        :return: MPG value
        """
        return round(ConversionUtils.MAGIC_NUMBER / (lkm * 100), 2)

    @staticmethod
    def convert_m_to_km(meters: float) -> float:
        """
        Convert meters to kms
        :param meters: Meters
        :return: Kms
        """
        return round(meters / 1000, 2)

    @staticmethod
    def convert_m_to_miles(meters: float) -> float:
        """
        Convert meters to miles
        :param meters: Meters
        :return: Miles
        """
        return round(meters / 1609, 2)

    # Decorator pattern (lines 69-99)
    @staticmethod
    def get_suffix(metric_choice: int) -> str:
        """
        Get suffix per metric choice
        :param metric_choice: Metric choice
        :return: Suffix
        """
        method = ConversionUtils.get_empty_suffix()
        if metric_choice == ConversionUtils.MPG:
            method = ConversionUtils.get_mpg_suffix()
        elif metric_choice == ConversionUtils.L_PER_100KM:
            method = ConversionUtils.get_l_100km_suffix()
        elif metric_choice == ConversionUtils.L_PER_KM:
            method = ConversionUtils.get_l_km_suffix()
        return method

    @staticmethod
    def get_mpg_suffix():
        return ConversionUtils.MPG_SUFFIX

    @staticmethod
    def get_l_100km_suffix():
        return ConversionUtils.L_PER_100KM_SUFFIX

    @staticmethod
    def get_l_km_suffix():
        return ConversionUtils.L_PER_KM_SUFFIX

    @staticmethod
    def get_empty_suffix():
        return ""
