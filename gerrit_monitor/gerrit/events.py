from abc import ABC, abstractmethod
from gerrit import structures


class Event(ABC):
    def __init__(self, json):
        self.json = json

    @abstractmethod
    def to_string(self):
        pass


class AssigneeChanged(Event):
    def to_string(self):
        pass


class ChangeAbandoned(Event):
    def to_string(self):
        pass


class ChangeDeleted(Event):
    def to_string(self):
        pass


class ChangeMerged(Event):
    def to_string(self):
        pass


class ChangeRestored(Event):
    def to_string(self):
        pass


class CommentAdded(Event):
    def to_string(self):
        change = structures.Change(self.json["change"])
        return change.topic


class DroppedOutput(Event):
    def to_string(self):
        pass


class HashtagsChanged(Event):
    def to_string(self):
        pass


class ProjectCreated(Event):
    def to_string(self):
        pass


class PatchsetCreated(Event):
    def to_string(self):
        pass


class RefReplicated(Event):
    def to_string(self):
        pass


class RefReplicationDone(Event):
    def to_string(self):
        pass


class RefReplicationScheduled(Event):
    def to_string(self):
        pass


class RefUpdated(Event):
    def to_string(self):
        pass


class ReviewerAdded(Event):
    def to_string(self):
        pass


class ReviewerDeleted(Event):
    def to_string(self):
        pass


class TopicChanged(Event):
    def to_string(self):
        pass


class VoteDeleted(Event):
    def to_string(self):
        pass


class WipStateChanged(Event):
    def to_string(self):
        pass


class PrivateStateChanged(Event):
    def to_string(self):
        pass


def create_event(json):
    event_type = json["type"]
    if event_type in _events_map:
        return _events_map[event_type](json)


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
