import hashlib

class Hash:
    @staticmethod
    def by_file(path):
        hash_md5 = hashlib.md5()

        # Abre o arquivo em modo de leitura binária ('rb')
        with open(path, "rb") as f:
            # Lê o arquivo em blocos (por exemplo, 4096 bytes) e atualiza o hash
            for bloco in iter(lambda: f.read(4096), b""):
                hash_md5.update(bloco)

        # Retorna o hash MD5 em formato hexadecimal
        return hash_md5.hexdigest()
