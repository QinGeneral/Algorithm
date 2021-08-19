class Solution {
    public String simplifyPath(String path) {
        path = path.replace("//", "/");
        if (path.charAt(path.length() - 1) == '/') {
            path = path.substring(0, path.length() - 1);
        }
        String[] pathes= path.split("/");
        ArrayList<String> pes = new ArrayList<>();
        for (int i = 0; i < pathes.length; i++) {
            System.out.println(pathes[i]);
            if (pathes[i].length() == 0) {
                continue;
            }
            if (pathes[i].equals(".")) {
                continue;
            } else if (pathes[i].equals("..")) {
                if (pes.size() > 0) {
                    pes.remove(pes.size() - 1);
                }
            } else {
                pes.add(pathes[i]);
            }
        }
        if (pes.size() == 0) {
            return "/";
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < pes.size(); i++) {
            result.append("/" + pes.get(i));
        }
        return result.toString();
    }
}