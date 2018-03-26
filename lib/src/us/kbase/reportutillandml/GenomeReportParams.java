
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
 * <p>Original spec-file type: GenomeReportParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "genome_input_ref",
    "workspace_name",
    "report_format"
})
public class GenomeReportParams {

    @JsonProperty("genome_input_ref")
    private String genomeInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("report_format")
    private String reportFormat;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("genome_input_ref")
    public String getGenomeInputRef() {
        return genomeInputRef;
    }

    @JsonProperty("genome_input_ref")
    public void setGenomeInputRef(String genomeInputRef) {
        this.genomeInputRef = genomeInputRef;
    }

    public GenomeReportParams withGenomeInputRef(String genomeInputRef) {
        this.genomeInputRef = genomeInputRef;
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

    public GenomeReportParams withWorkspaceName(String workspaceName) {
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

    public GenomeReportParams withReportFormat(String reportFormat) {
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
        return ((((((((("GenomeReportParams"+" [genomeInputRef=")+ genomeInputRef)+", workspaceName=")+ workspaceName)+", reportFormat=")+ reportFormat)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
