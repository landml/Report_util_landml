
package us.kbase.reportutillandml;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FeatSeqReportParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "feature_sequence_input_ref",
    "workspace_name",
    "report_format"
})
public class FeatSeqReportParams {

    @JsonProperty("feature_sequence_input_ref")
    private String featureSequenceInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("report_format")
    private String reportFormat;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("feature_sequence_input_ref")
    public String getFeatureSequenceInputRef() {
        return featureSequenceInputRef;
    }

    @JsonProperty("feature_sequence_input_ref")
    public void setFeatureSequenceInputRef(String featureSequenceInputRef) {
        this.featureSequenceInputRef = featureSequenceInputRef;
    }

    public FeatSeqReportParams withFeatureSequenceInputRef(String featureSequenceInputRef) {
        this.featureSequenceInputRef = featureSequenceInputRef;
        return this;
    }

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public FeatSeqReportParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("report_format")
    public String getReportFormat() {
        return reportFormat;
    }

    @JsonProperty("report_format")
    public void setReportFormat(String reportFormat) {
        this.reportFormat = reportFormat;
    }

    public FeatSeqReportParams withReportFormat(String reportFormat) {
        this.reportFormat = reportFormat;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("FeatSeqReportParams"+" [featureSequenceInputRef=")+ featureSequenceInputRef)+", workspaceName=")+ workspaceName)+", reportFormat=")+ reportFormat)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
