type ChannelType = {
  email?: NotificationBase;
  slack?: NotificationBase;
};

type NotificationBase = {
  recipients: string[];
};

type NotificationType = {
  template: NotificationTemplate;
  channels: ChannelType;
  data?: any;
};
