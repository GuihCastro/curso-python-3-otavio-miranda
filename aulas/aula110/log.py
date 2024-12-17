from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def _log_error(self, msg):
        return self._log(f'ERRO: {msg}')

    def _log_success(self, msg):
        return self._log(f'SUCESSO: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formated_msg = f'{msg} ({self.__class__.__name__})\n'
        print(f'Salvando no log: {formated_msg}')
        with LOG_FILE.open('+a', encoding='utf-8') as log:
            log.write(formated_msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print._log_success('Ontem eu comi pipoca com sal')
    log_print._log_error('Fiquei todo empanzinado. Tô mal, mal, mal, mal...')

    log_to_file = LogFileMixin()
    log_to_file._log_success('Ontem eu comi pipoca com sal')
    log_to_file._log_error('Fiquei todo empanzinado. Tô mal, mal, mal, mal...')
