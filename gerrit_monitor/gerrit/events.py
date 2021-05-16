from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, json):
        self.json = json

    @abstractmethod
    def to_string(self):
        pass


class AssigneeChanged:
    def to_string(self):
        pass


class ChangeAbandoned:
    def to_string(self):
        pass


class ChangeDeleted:
    def to_string(self):
        pass


class ChangeMerged:
    def to_string(self):
        pass


class ChangeRestored:
    def to_string(self):
        pass


class CommentAdded:
    def to_string(self):
        pass


class DroppedOutput:
    def to_string(self):
        pass


class HashtagsChanged:
    def to_string(self):
        pass


class ProjectCreated:
    def to_string(self):
        pass


class PatchsetCreated:
    def to_string(self):
        pass


class RefReplicated:
    def to_string(self):
        pass


class RefReplicationDone:
    def to_string(self):
        pass


class RefReplicationScheduled:
    def to_string(self):
        pass


class RefUpdated:
    def to_string(self):
        pass


class ReviewerAdded:
    def to_string(self):
        pass


class ReviewerDeleted:
    def to_string(self):
        pass


class TopicChanged:
    def to_string(self):
        pass


class VoteDeleted:
    def to_string(self):
        pass


class WipStateChanged:
    def to_string(self):
        pass


class PrivateStateChanged:
    def to_string(self):
        pass


def create_event(gerrit_type):
    if gerrit_type in _events_map:
        return _events_map[gerrit_type]()


_events_map = {
    "assignee-changed": AssigneeChanged,
    "change-abandoned": ChangeAbandoned,
    "change-deleted": ChangeDeleted,
    "change-merged": ChangeMerged,
    "change-restored": ChangeRestored,
    "comment-added": CommentAdded,
    "dropped-output": DroppedOutput,
    "hashtags-changed": HashtagsChanged,
    "project-created": ProjectCreated,
    "patchset-created": PatchsetCreated,
    "ref-updated": RefUpdated,
    "reviewer-added": ReviewerAdded,
    "reviewer-deleted": ReviewerDeleted,
    "topic-changed": TopicChanged,
    "vote-deleted": VoteDeleted,
    "wip-state-changed": WipStateChanged,
    "private-state-changed": PrivateStateChanged,
}
