
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
 * <p>Original spec-file type: GenomeSetReportParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "genomeset_input_ref",
    "workspace_name",
    "report_format"
})
public class GenomeSetReportParams {

    @JsonProperty("genomeset_input_ref")
    private String genomesetInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("report_format")
    private String reportFormat;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("genomeset_input_ref")
    public String getGenomesetInputRef() {
        return genomesetInputRef;
    }

    @JsonProperty("genomeset_input_ref")
    public void setGenomesetInputRef(String genomesetInputRef) {
        this.genomesetInputRef = genomesetInputRef;
    }

    public GenomeSetReportParams withGenomesetInputRef(String genomesetInputRef) {
        this.genomesetInputRef = genomesetInputRef;
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

    public GenomeSetReportParams withWorkspaceName(String workspaceName) {
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

    public GenomeSetReportParams withReportFormat(String reportFormat) {
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
        return ((((((((("GenomeSetReportParams"+" [genomesetInputRef=")+ genomesetInputRef)+", workspaceName=")+ workspaceName)+", reportFormat=")+ reportFormat)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
