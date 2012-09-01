import csv

class Row(object):
    COLUMNS = []

    def __init__(self, raw_row = []):
        self.__raw_row__ = raw_row
        for i in range(len(raw_row), len(self.get_columns())):
            self.__raw_row__.append(None)

    @staticmethod
    def add_column(column_name, position=None):
        if position:
            self.get_columns().insert(position, column_name)
        else:
            self.get_columns().append(column_name)

    def get_value(self, column_name):
        return self.__raw_row__[self.get_columns().index(column_name)]

    def add_data(self, column_name, data):
        self.__raw_row__[self.get_columns().index(column_name)] = data

    def get_data_as_dict(self):
        data = {}
        for column in self.get_columns():
            data[column] = self.__raw_row__[self.get_columns().index(column)]
        return data

    def get_raw_data(self):
        return self.__raw_row__


class StatusRow(Row):
    JOB = 'job'
    TOTAL_SOURCE = 'total source'
    TOTAL_TARGET = 'total target'
    COPIED = 'copied'
    UPDATED = 'updated'
    FAILED = 'failed'
    ERROR = 'ERROR'
    COLUMNS = [JOB, TOTAL_SOURCE, TOTAL_TARGET, COPIED, UPDATED, FAILED, ERROR]

    def __init__(self, raw_row = []):
        super(StatusRow, self).__init__(raw_row)

    @staticmethod
    def get_columns():
        return StatusRow.COLUMNS

class DomainUsersRow(Row):
    USER_SOURCE = 'origin'
    USER_DESTINATION = 'destination'
    PASSWORD = 'password'
    MIGRATE = 'migrate'
    COLUMNS = [USER_SOURCE, USER_DESTINATION, PASSWORD, MIGRATE]

    def __init__(self, raw_row = []):
        super(DomainUsersRow, self).__init__(raw_row)


    def get_info(self):
        return {DomainUsersRow.USER_SOURCE: self.__raw_row__[DomainUsersRow.COLUMNS.index(DomainUsersRow.USER_SOURCE)],
                DomainUsersRow.USER_DESTINATION: self.__raw_row__[DomainUsersRow.COLUMNS.index(DomainUsersRow.USER_DESTINATION)],
                DomainUsersRow.PASSWORD: self.__raw_row__[DomainUsersRow.COLUMNS.index(DomainUsersRow.PASSWORD)],
                DomainUsersRow.MIGRATE: self.__raw_row__[DomainUsersRow.COLUMNS.index(DomainUsersRow.MIGRATE)]}

    @staticmethod
    def get_columns():
        return DomainUsersRow.COLUMNS

class DomainGroupRow(Row):
    GROUP_ID = 'groupid'
    GROUPNAME = 'groupName'
    DESCRIPTION = 'description'
    EMAIL_PERMISSION = 'emailPermission'
    MEMBERS = 'members'
    MEMBERS_IN_DESTINATION = 'members_in_destination'
    RESULT = 'result'
    COLUMNS = [GROUP_ID, GROUPNAME, DESCRIPTION, EMAIL_PERMISSION, MEMBERS, MEMBERS_IN_DESTINATION, RESULT]

    def __init__(self, raw_row = []):
        super(DomainGroupRow, self).__init__(raw_row)


    def get_info(self):
        return {DomainGroupRow.GROUP_ID: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.GROUP_ID)],
                DomainGroupRow.GROUPNAME: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.GROUPNAME)],
                DomainGroupRow.DESCRIPTION: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.DESCRIPTION)],
                DomainGroupRow.MEMBERS: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.MEMBERS)],
                DomainGroupRow.MEMBERS_IN_DESTINATION: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.MEMBERS_IN_DESTINATION)],
                DomainGroupRow.EMAIL_PERMISSION: self.__raw_row__[DomainGroupRow.COLUMNS.index(DomainGroupRow.EMAIL_PERMISSION)]}

    @staticmethod
    def get_columns():
        return DomainGroupRow.COLUMNS

class DomainGroupSettingsRow(Row):
    GROUP_ID = 'groupid'
    RESULT = 'result'
    COLUMNS = [GROUP_ID, RESULT]

    def __init__(self, raw_row = []):
        super(DomainGroupSettingsRow, self).__init__(raw_row)

    @staticmethod
    def get_columns():
        return DomainGroupSettingsRow.COLUMNS


class ForwardUsersRow(Row):
    USER_SOURCE = 'origin'
    USER_DESTINATION = 'destination'
    COLUMNS = [USER_SOURCE, USER_DESTINATION]

    def __init__(self, raw_row = []):
        super(ForwardUsersRow, self).__init__(raw_row)


    def get_info(self):
        return {ForwardUsersRow.USER_SOURCE: self.__raw_row__[ForwardUsersRow.COLUMNS.index(ForwardUsersRow.USER_SOURCE)],
                ForwardUsersRow.USER_DESTINATION: self.__raw_row__[ForwardUsersRow.COLUMNS.index(ForwardUsersRow.USER_DESTINATION)]}

    @staticmethod
    def get_columns():
        return ForwardUsersRow.COLUMNS


class UsersToMigrateRow(Row):
    USER_SOURCE = 'origin'
    FAMILY_NAME = 'family_name'
    GIVEN_NAME = 'given_name'
    QUOTA_LIMIT = 'quota_limit'
    SUSPENDED = 'suspended'
    USER_DESTINATION = 'destination'
    PASSWORD = 'password'
    NICKNAMES = 'nicknames'
    RESULT = 'result'
    COLUMNS = [USER_SOURCE, USER_DESTINATION, FAMILY_NAME, GIVEN_NAME, QUOTA_LIMIT, SUSPENDED, PASSWORD, NICKNAMES, RESULT]

    def __init__(self, raw_row = []):
        super(UsersToMigrateRow, self).__init__(raw_row)


    @staticmethod
    def get_columns():
        return UsersToMigrateRow.COLUMNS

class UsersCopyRow(Row):
    USER1 = 'user1'
    USER2 = 'user2'
    PASSWORD = 'password'
    USER_CREATED = 'user_created'
    NICKNAMES = 'nicknames'
    COLUMNS = [USER1, USER2, PASSWORD, USER_CREATED, NICKNAMES]

    def __init__(self, raw_row = []):
        super(UsersCopyRow, self).__init__(raw_row)


    def get_users_data(self):
        return {UsersCopyRow.USER1: self.__raw_row__[UsersCopyRow.COLUMNS.index(UsersCopyRow.USER1)],
                UsersCopyRow.USER2: self.__raw_row__[UsersCopyRow.COLUMNS.index(UsersCopyRow.USER2)]}

    @staticmethod
    def get_columns():
        return UsersCopyRow.COLUMNS

class UsersNicknameRow(Row):
    USER = 'user'
    NICKNAME_USER = 'nickname'
    CREATED = 'created'
    ERROR = "error"
    COLUMNS = [USER, NICKNAME_USER, CREATED, ERROR]

    def __init__(self, raw_row = []):
        super(UsersNicknameRow, self).__init__(raw_row)

    def get_users_data(self):
        return {UsersNicknameRow.USER: self.__raw_row__[UsersNicknameRow.COLUMNS.index(UsersNicknameRow.USER)],
                UsersNicknameRow.NICKNAME_USER: self.__raw_row__[UsersNicknameRow.COLUMNS.index(UsersNicknameRow.NICKNAME_USER)]}

    @staticmethod
    def get_columns():
        return UsersNicknameRow.COLUMNS


class DeleteUserRow(object):
    USER = 'user'

    def __init__(self, columns, raw_row):
        self.__raw_row__ = raw_row
        self.columns = columns

    def get_users_data(self):
        self.columns.index(DeleteUserRow.USER)
        return {DeleteUserRow.USER: self.__raw_row__[self.columns.index(DeleteUserRow.USER)]}

    def add_raw_data(self, data):
        self.__raw_row__.append(data)

    def get_raw_data(self):
        return self.__raw_row__

    @staticmethod
    def get_columns():
        return ['user_deleted']

class UsersCheckerRow(object):
    FIRST_USER = 'user1'
    FIRST_PASS = 'pass1'
    FIRST_HOST = 'host1'
    FIRST_KEY = 'ckey1'
    FIRST_SECRET = 'csecret1'
    SECOND_USER = 'user2'
    SECOND_PASS = 'pass2'
    SECOND_HOST = 'host2'
    SECOND_KEY = 'ckey2'
    SECOND_SECRET = 'csecret2'

    USER_NAME = 'user'
    USER_PASS = 'pass'
    USER_HOST = 'host'
    USER_KEY = 'ckey'
    USER_SECRET = 'csecret'

    def __init__(self, columns, raw_row):
        self.__raw_row__ = raw_row
        self.columns = columns

    def get_data_user1(self):
        try:
            self.columns.index(UsersCheckerRow.FIRST_KEY)
            return {UsersCheckerRow.USER_NAME: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_USER)],
                    UsersCheckerRow.USER_KEY: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_KEY)],
                    UsersCheckerRow.USER_SECRET: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_SECRET)]}
        except ValueError:
            return {UsersCheckerRow.USER_NAME: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_USER)],
                    UsersCheckerRow.USER_PASS: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_PASS)],
                    UsersCheckerRow.USER_HOST: self.__raw_row__[self.columns.index(UsersCheckerRow.FIRST_HOST)]}

    def get_data_user2(self):
        try:
            self.columns.index(UsersCheckerRow.SECOND_KEY)
            return {UsersCheckerRow.USER_NAME: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_USER)],
                    UsersCheckerRow.USER_KEY: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_KEY)],
                    UsersCheckerRow.USER_SECRET: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_SECRET)]}
        except ValueError:
            return {UsersCheckerRow.USER_NAME: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_USER)],
                    UsersCheckerRow.USER_PASS: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_PASS)],
                    UsersCheckerRow.USER_HOST: self.__raw_row__[self.columns.index(UsersCheckerRow.SECOND_HOST)]}

    def add_raw_data(self, data):
        self.__raw_row__.append(data)

    def get_raw_data(self):
        return self.__raw_row__

    @staticmethod
    def get_columns():
        return ['user1_ok', 'user2_ok']


class CSVMigrations(object):
    def __init__(self, type, file = None):
        if file:
            self.reader = csv.reader(open(file, 'rU') if isinstance(file, str) else file) 
            self.columns = self.reader.next()
        self.rows = []
        self.row_type = type

    def new_row(self, data=None):
        data = data or []
        row = self.row_type(data)
        self.rows.append(row)
        return row

    def next_row(self):
        for i, raw_row in enumerate(self.reader):
            row = self.new_row(raw_row)
            yield row

    def look_for(self, column, value, app_filter):
        for row in self.rows:
            if app_filter(row.get_value(column), value):
                return row
        return None

    def write_row(self, row):
        self.rows.append(row)

    def save_results(self, dest= 'output.csv'):
        with open(dest, 'wb') as f:
            self.writer = csv.writer(f)
            self.writer.writerow(self.row_type.get_columns())
            for row in self.rows:
                self.writer.writerow(row.get_raw_data())

    @staticmethod
    def create_file(data, dest):
        writer = csv.writer(open(dest, 'wb'))
        for row in data:
            writer.writerow(row)

