class Change:
    def __init__(self, json):
        self.json = json

    @property
    def project(self):
        return self.json.get("project")

    @property
    def branch(self):
        return self.json.get("branch")

    @property
    def topic(self):
        return self.json.get("topic")

    @property
    def id(self):
        return self.json.get("id")

    @property
    def number(self):
        return self.json.get("number")

    @property
    def subject(self):
        return self.json.get("subject")

    @property
    def owner(self):
        return self.json.get("owner")

    @property
    def url(self):
        return self.json.get("url")

    @property
    def commitMessage(self):
        return self.json.get("commitMessage")

    @property
    def hashtags(self):
        return self.json.get("hashtags")

    @property
    def createdOn(self):
        return self.json.get("createdOn")

    @property
    def lastUpdated(self):
        return self.json.get("lastUpdated")

    @property
    def open(self):
        return self.json.get("open")

    @property
    def status(self):
        # NEW
        # MERGED
        # ABANDONED
        return self.json.get("status")

    @property
    def private(self):
        return self.json.get("private")

    @property
    def wip(self):
        return self.json.get("wip")

    @property
    def comments(self):
        return self.json.get("comments")

    @property
    def trackingIds(self):
        return self.json.get("trackingIds")

    @property
    def currentPatchSet(self):
        return self.json.get("currentPatchSet")

    @property
    def patchSets(self):
        return self.json.get("patchSets")

    @property
    def dependsOn(self):
        return self.json.get("dependsOn")

    @property
    def neededBy(self):
        return self.json.get("neededBy")

    @property
    def submitRecords(self):
        return self.json.get("submitRecords")

    @property
    def allReviewers(self):
        return self.json.get("allReviewers")


class Trackingid:
    def __init__(self, json):
        self.json = json

    @property
    def system(self):
        return self.json.get("system")

    @property
    def id(self):
        return self.json.get("id")


class Account:
    def __init__(self, json):
        self.json = json

    @property
    def name(self):
        return self.json.get("name")

    @property
    def email(self):
        return self.json.get("email")

    @property
    def username(self):
        return self.json.get("username")


class PatchSet:
    def __init__(self, json):
        self.json = json

    @property
    def number(self):
        return self.json.get("number")

    @property
    def revision(self):
        return self.json.get("revision")

    @property
    def parents(self):
        return self.json.get("parents")

    @property
    def ref(self):
        return self.json.get("ref")

    @property
    def uploader(self):
        return self.json.get("uploader")

    @property
    def author(self):
        return self.json.get("author")

    @property
    def createdOn(self):
        return self.json.get("createdOn")

    @property
    def kind(self):
        # REWORK
        # TRIVIAL_REBASE
        # MERGE_FIRST_PARENT_UPDATE
        # NO_CODE_CHANGE
        # NO_CHANGE
        return self.json.get("kind")

    @property
    def approvals(self):
        return self.json.get("approvals")

    @property
    def comments(self):
        return self.json.get("comments")

    @property
    def files(self):
        return self.json.get("files")

    @property
    def sizeInsertions(self):
        return self.json.get("sizeInsertions")

    @property
    def sizeDeletions(self):
        return self.json.get("sizeDeletions")


class Approval:
    def __init__(self, json):
        self.json = json

    @property
    def type(self):
        return self.json.get("type")

    @property
    def description(self):
        return self.json.get("description")

    @property
    def value(self):
        return self.json.get("value")

    @property
    def oldValue(self):
        return self.json.get("oldValue")

    @property
    def grantedOn(self):
        return self.json.get("grantedOn")

    @property
    def by(self):
        return self.json.get("by")


class RefUpdate:
    def __init__(self, json):
        self.json = json

    @property
    def oldRev(self):
        return self.json.get("oldRev")

    @property
    def newRev(self):
        return self.json.get("newRev")

    @property
    def refName(self):
        return self.json.get("refName")

    @property
    def project(self):
        return self.json.get("project")


class SubmitRecord:
    def __init__(self, json):
        self.json = json

    @property
    def status(self):
        # OK
        # NOT_READY
        # RULE_ERROR
        return self.json.get("status")

    @property
    def labels(self):
        return self.json.get("labels")

    @property
    def requirements(self):
        return self.json.get("requirements")


class Requirement:
    def __init__(self, json):
        self.json = json

    @property
    def fallbackText(self):
        return self.json.get("fallbackText")

    @property
    def type(self):
        return self.json.get("type")

    @property
    def data(self):
        return self.json.get("data")


class Label:
    def __init__(self, json):
        self.json = json

    @property
    def label(self):
        return self.json.get("label")

    @property
    def status(self):
        # OK
        # REJECT
        # NEED
        # MAY
        # IMPOSSIBLE
        return self.json.get("status")

    @property
    def by(self):
        return self.json.get("by")


class Dependency:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get("id")

    @property
    def number(self):
        return self.json.get("number")

    @property
    def revision(self):
        return self.json.get("revision")

    @property
    def ref(self):
        return self.json.get("ref")

    @property
    def isCurrentPatchSet(self):
        return self.json.get("isCurrentPatchSet")


class Message:
    def __init__(self, json):
        self.json = json

    @property
    def timestamp(self):
        return self.json.get("timestamp")

    @property
    def reviewer(self):
        return self.json.get("reviewer")

    @property
    def message(self):
        return self.json.get("message")


class PatchsetComment:
    def __init__(self, json):
        self.json = json

    @property
    def file(self):
        return self.json.get("file")

    @property
    def line(self):
        return self.json.get("line")

    @property
    def reviewer(self):
        return self.json.get("reviewer")

    @property
    def message(self):
        return self.json.get("message")


class File:
    def __init__(self, json):
        self.json = json

    @property
    def file(self):
        return self.json.get("file")

    @property
    def fileOld(self):
        return self.json.get("fileOld")

    @property
    def type(self):
        # ADDED
        # MODIFIED
        # DELETED
        # RENAMED
        # COPIED
        # REWRITE
        return self.json.get("type")

    @property
    def insertions(self):
        return self.json.get("insertions")

    @property
    def deletions(self):
        return self.json.get("deletions")
