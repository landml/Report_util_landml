
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
 * <p>Original spec-file type: TreeReportParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "tree_input_ref",
    "workspace_name",
    "report_format"
})
public class TreeReportParams {

    @JsonProperty("tree_input_ref")
    private String treeInputRef;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("report_format")
    private String reportFormat;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("tree_input_ref")
    public String getTreeInputRef() {
        return treeInputRef;
    }

    @JsonProperty("tree_input_ref")
    public void setTreeInputRef(String treeInputRef) {
        this.treeInputRef = treeInputRef;
    }

    public TreeReportParams withTreeInputRef(String treeInputRef) {
        this.treeInputRef = treeInputRef;
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

    public TreeReportParams withWorkspaceName(String workspaceName) {
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

    public TreeReportParams withReportFormat(String reportFormat) {
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
        return ((((((((("TreeReportParams"+" [treeInputRef=")+ treeInputRef)+", workspaceName=")+ workspaceName)+", reportFormat=")+ reportFormat)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
