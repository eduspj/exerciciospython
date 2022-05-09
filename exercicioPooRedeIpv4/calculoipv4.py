import re  # Expressões regulares


class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

        print(f'IP =        {self.ip}')
        print(f'Mascara =   {self.mascara}')
        print(f'Rede =      {self.rede}')
        print(f'Brodcast =  {self.broadcast}')
        print(f'Prefixo =   {self.prefixo}')
        print(f'Nº de IPs = {self.num_ips}')

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def num_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido')
        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        if not self._valida_ip(valor):
            raise ValueError('Máscara inválido')
        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro')
        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 bits')
        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._set_broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._set_broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._broadcast

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)