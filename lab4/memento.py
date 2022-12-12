class Memento:
    def __init__(self, editor, effect):
        self._editor = editor
        self._effect = effect

    def get_state(self):
        return self._effect


class PhotoEditor:
    def __init__(self, effect=None):
        self._effect = effect
        print(f'Current photo effects are {self._effect}')

    def add_effect(self, new_effect):
        print(f'Applied {new_effect} to photo')
        self._effect = new_effect

    def save(self):
        print('New photo effects are saved')
        return Memento(self, self._effect)

    def restore(self, memento):
        self._effect = memento.get_state()
        print(f'Restored previous state. Current photo effects: {self._effect}')


class StateManager:
    def __init__(self, editor):
        self._editor = editor
        self._history = []

    def backup(self):
        new_backup = self._editor.save()
        self._history.append(new_backup)

    def undo(self):
        print('Undoing some effects...')
        memento = self._history[-2]
        self._editor.restore(memento)


def client_code():
    print('Uploaded new photo to editor')
    photo = PhotoEditor()
    state_manager = StateManager(photo)
    print('')

    photo.add_effect('Black and White effect')
    state_manager.backup()
    print('')

    photo.add_effect('Higher lightness, lower contrast effects')
    state_manager.backup()
    print('')

    state_manager.undo()


def main():
    client_code()


if __name__ == '__main__':
    main()