package consumer;

import com.google.gson.Gson;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.annotation.TopicPartition;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Component;



@Component
class MessageListener {

    @Autowired
    SimpMessagingTemplate template;

    @Autowired
    Gson gson;
    private static final Logger LOGGER = LogManager.getLogger(MessageListener.class);

    @KafkaListener(
            topicPartitions = {
                    @TopicPartition(
                            topic = "cts-topic",
                            partitions = { "0", "2" }
                    )},
            topics = "cts-topic", groupId = "cts-select-partition-consumer-group")
    private void listen_to_selected_partitions(ConsumerRecord<String, String> record) {
        LOGGER.info("listen_to_selected_partitions");
        LOGGER.info("Message was in partition {}", record.partition());
        LOGGER.info("Message key was: {} and value: {}", record.key(), record.value());
        template.convertAndSend("/topic", gson.toJson(record));
    }

    /*@KafkaListener(
            topics = "cts-topic", groupId = "cts-select-partition-consumer-group")
    private void listen_to_all_partitions(ConsumerRecord<String, String> record) {
        LOGGER.info("listen_to_all_partitions");
        LOGGER.info("Message was in partition {}", record.partition());
        LOGGER.info("Message key was: {} and value: {}", record.key(), record.value());
        template.convertAndSend("/topic", gson.toJson(record));
    } */

}



